/* OS X version 1.0
   Clive Darke September 2014
*/

/* Version for QAPYTH3 exercises */
#include <stdio.h>
#include <sys/types.h>
#include <sys/sysctl.h>
#include <stdlib.h>

#include "Python.h"

/* Local prototypes */
static PyObject * getallprocs  (PyObject *self, PyObject *args);
static PyObject * getfirstproc (PyObject *self, PyObject *args);
static PyObject * getnextproc  (PyObject *self, PyObject *args);

/* Globals */
struct kinfo_proc *g_kprocbuf = NULL;
size_t g_numProcs = 0;
size_t g_index = 0;

// Local prototypes
void ExitFunc(void);

// Python Globals

/* Method table */
static PyMethodDef GetProcsMethods[] = {
    {"getallprocs",  getallprocs,  METH_VARARGS,"Get running processes."},
    {"getfirstproc", getfirstproc, METH_VARARGS,"Start of iteration of running processes."},
    {"getnextproc",  getnextproc,  METH_VARARGS,"Next iteration of running processes."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

/* required for Python 3 */
static struct PyModuleDef getprocs_module = {
   PyModuleDef_HEAD_INIT,
   "getprocs",   // name of module
   NULL,         // spam_doc, // module documentation, may be NULL
   -1,           // size of per-interpreter state of the module,
                 //  or -1 if the module keeps state in global variables.
   GetProcsMethods
};

/* -------------------------------------------------------------------------- */
void ExitFunc(void)
{
    if (g_kprocbuf) {
        free(g_kprocbuf);
        g_kprocbuf = NULL;
    }
}

/* Module entry point Python 3 */

PyMODINIT_FUNC PyInit_getprocs(void)
{
    Py_AtExit(ExitFunc);
    return PyModule_Create(&getprocs_module);
}


/* Module entry point Python 2

PyMODINIT_FUNC initgetprocs(void)
{
    (void) Py_InitModule("getprocs", GetProcsMethods);
}
*/

/* WORKER functions */
/* -------------------------------------------------------------------------- */

static PyObject * getallprocs(PyObject *self, PyObject *args)
{
    PyObject * RetnList = PyList_New(0);
    PyObject *tup = getfirstproc(self, args);

    do
    {
        //fprintf(stderr,"List size: %d\n",PyList_Size(RetnList));

        int iRetn = PyList_Append(RetnList, tup);
        if (iRetn == -1) {
            fprintf(stderr, "PyListAppend failed\n");
            Py_RETURN_FALSE;
        }
        Py_DECREF(tup);
        tup = getnextproc(self, args);

    }
    while (tup != Py_False);

    return RetnList;
}

/* -------------------------------------------------------------------------- */

static PyObject * getfirstproc(PyObject *self, PyObject *args)
{
    int mib[4] = { CTL_KERN, KERN_PROC, KERN_PROC_ALL, 0};
    size_t buffSize = 0;
    size_t originalBuffSize = 0;
    int retn = 0;

    /* Get buffer size */
    retn = sysctl(mib, 4, NULL, &buffSize, NULL, 0);
    if (retn != 0) {
        perror("Size sysctl");
        Py_RETURN_FALSE;
    }

    //printf("buffSize: %zu, buffers: %zu\n",
    //        buffSize, buffSize/sizeof(struct kinfo_proc));

    g_kprocbuf = malloc(buffSize);
    if (g_kprocbuf == NULL) {
        perror("malloc 1");
        Py_RETURN_FALSE;
    }

    originalBuffSize = buffSize;

    /* Get procs */
    retn = sysctl(mib, 4, g_kprocbuf, &buffSize, NULL, 0);
    if (retn != 0) {
        perror("Size sysctl");
        Py_RETURN_FALSE;
    }

    /* Number of procs may have changed between calls */
    if (buffSize > originalBuffSize)  {
        /* Need to allocate more memory */
        free(g_kprocbuf);
        g_kprocbuf = malloc(buffSize);
        if (g_kprocbuf == NULL) {
            perror("malloc 2");
            Py_RETURN_FALSE;
        }
    }

    g_numProcs = buffSize/sizeof(struct kinfo_proc);
    g_index = 0;

    return getnextproc(self, args);
}

/* -------------------------------------------------------------------------- */

static PyObject * getnextproc(PyObject *self, PyObject *args)
{
     if (g_index < g_numProcs) {
        /*
        printf("%d %d %s\n",
            g_kprocbuf[g_index].kp_proc.p_pid,
            g_kprocbuf[g_index].kp_eproc.e_ppid,
            g_kprocbuf[g_index].kp_proc.p_comm);
        */
        PyObject *tup = Py_BuildValue("(iis)",
                        g_kprocbuf[g_index].kp_proc.p_pid,
                        g_kprocbuf[g_index].kp_eproc.e_ppid,
                        g_kprocbuf[g_index].kp_proc.p_comm);

        g_index++;
        return tup;
     }
     else {
        Py_RETURN_FALSE;
    }
}

/* -------------------------------------------------------------------------- */

