/* Version for QAPYTH3 exercises */
#define _WIN32_WINNT 0x0501
#include <windows.h>
#include <tlhelp32.h>
#include <psapi.h>
#include "Python.h"

/* Local prototypes */
static PyObject * GetPids(void);
static void ProcessError(const char *szMessage);
static PyObject * GetAllProcs  (PyObject *self, PyObject *args);
static PyObject * GetFirstProc (PyObject *self, PyObject *args);
static PyObject * GetNextProc  (PyObject *self, PyObject *args);

/* Globals */
HANDLE g_hToolSnapshot = INVALID_HANDLE_VALUE;
PROCESSENTRY32 g_Pe32 = {0};

// Local prototypes

// Python Globals
static PyObject *GetProcsError;                   // TODO
static PyMethodDef GetProcsMethods[] = {
    {"getallprocs",  GetAllProcs,  METH_VARARGS,"Get running processes."},
    {"getfirstproc", GetFirstProc, METH_VARARGS,"Start of iteration of running processes."},
	{"getnextproc",  GetNextProc,  METH_VARARGS,"Next iteration of running processes."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef getprocs_module = {
   PyModuleDef_HEAD_INIT,
   "getprocs",   /* name of module */
   NULL,     /* spam_doc, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   GetProcsMethods
};

/* --------------------------------------------------------------------------------------------------------- */

void ExitFunc(void)
{
   if (g_hToolSnapshot != INVALID_HANDLE_VALUE) {
	   CloseHandle(g_hToolSnapshot);
   }
}

/* Module entry point */

PyMODINIT_FUNC PyInit_getprocs(void)
{
	Py_AtExit(ExitFunc);

    return PyModule_Create(&getprocs_module);
}

/* WORKER functions */
/* --------------------------------------------------------------------------------------------------------- */

static PyObject * GetAllProcs(PyObject *self, PyObject *args)
{
    return GetPids();
}

/* --------------------------------------------------------------------------------------------------------- */

static PyObject * GetFirstProc(PyObject *self, PyObject *args)
{
    BOOL bResult;
	PyObject *tup;

    g_hToolSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (g_hToolSnapshot == INVALID_HANDLE_VALUE) {
       Py_RETURN_FALSE;
    }

    g_Pe32.dwSize = sizeof(PROCESSENTRY32);

    bResult = Process32First(g_hToolSnapshot, &g_Pe32);
    if (!bResult) {
       Py_RETURN_FALSE;
    }

	tup = Py_BuildValue("(iis)", g_Pe32.th32ProcessID, g_Pe32.th32ParentProcessID, g_Pe32.szExeFile);
    return tup;
}

/* --------------------------------------------------------------------------------------------------------- */

static PyObject * GetNextProc(PyObject *self, PyObject *args)
{
	BOOL bRetn;

	if (g_hToolSnapshot == INVALID_HANDLE_VALUE)
        Py_RETURN_FALSE;

	bRetn = Process32Next(g_hToolSnapshot, &g_Pe32);
    if (bRetn)
	{
        PyObject *tup = Py_BuildValue("(iis)", g_Pe32.th32ProcessID, g_Pe32.th32ParentProcessID, g_Pe32.szExeFile);
        return tup;
    }
	else
	{
		CloseHandle(g_hToolSnapshot);
		g_hToolSnapshot = INVALID_HANDLE_VALUE;
		Py_RETURN_FALSE;
	}
}

/* --------------------------------------------------------------------------------------------------------- */

static PyObject * GetPids(void)
{
    DWORD dwRetn = 0;
    int PIDs = 0;
    HANDLE hToolSnapshot;
    PROCESSENTRY32 Pe32 = {0};
    BOOL bResult;
	PyObject * RetnList = PyList_New(0);

    hToolSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hToolSnapshot == INVALID_HANDLE_VALUE) {
       Py_RETURN_FALSE;
    }

    Pe32.dwSize = sizeof(PROCESSENTRY32);

    bResult = Process32First(hToolSnapshot, &Pe32);

    if (!bResult) {
       Py_RETURN_FALSE;
    }

    do
	{
        int iRetn;

        PyObject *tup = Py_BuildValue("(iis)", Pe32.th32ProcessID, Pe32.th32ParentProcessID, Pe32.szExeFile);

		//fprintf(stderr,"List size: %d\n",PyList_Size(RetnList));

		iRetn = PyList_Append(RetnList, tup);
		if (iRetn == -1) {
			fprintf(stderr, "PyListAppend failed\n");
			Py_RETURN_FALSE;
		}
        Py_DECREF(tup);

    }
	while (Process32Next(hToolSnapshot, &Pe32));

    /* Expected */
    if (GetLastError() == ERROR_NO_MORE_FILES) {
        SetLastError(ERROR_SUCCESS);
    }

    CloseHandle(hToolSnapshot);
    return RetnList;
}

/* --------------------------------------------------------------------------------------------------------- */

static void ProcessError(const char *szMessage)
{
    char* buffer;
    DWORD dwErr = GetLastError();

    FormatMessage(
                FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
                0,
                dwErr,
                MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), // Default language
                (LPTSTR) &buffer,
                0,
                0);

    if (dwErr != ERROR_SUCCESS)
       printf("%s(%d): %s", szMessage, dwErr, buffer);
    else
       printf("%s\n", szMessage);

    LocalFree(buffer);
}

/* --------------------------------------------------------------------------------------------------------- */
