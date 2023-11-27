#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to struct
 *
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *begin = list;
	listint_t *end = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (end != NULL && end->next != NULL)
	{
		if (begin == end)
			return (1);
		begin = begin->next;
		end = end->next->next;
	}
	return (0);
}
