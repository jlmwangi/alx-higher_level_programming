#include <python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - print basic info about python
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	lint n;
	PyListObject *obj = (PyListObject *)p;
	long int size =- PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (n = 0; n < size; n++)
		printf("Element %n: %s\n", n, Py_TYPE(obj->ob_item[n])->tp_name);
}
