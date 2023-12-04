#include "lists.h"
/**
 * reverse_list - reverse linked list
 * @head: pointer to first node
 *
 */
void reverse_list(listint_t **head)
{
	listint_t *now = *head;
	listint_t *prev = *NULL, *next = NULL;

	while (now)
	{
		next = now->next;
		now->next = prev;
		prev = now;
		now = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks singly linked list
 * @head: pointer to pointer to listint_t
 *
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *dupl = NULL;
	listint_t *low = *head, *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dupl = low->next;
			break;
		}
		if (!fast->next)
		{
			dupl = low->next->next;
			break;
		}
		low = low->next;
	}
	reverse_list(&dupl);
	while (dupl && temp)
	{
		if (temp->n == dupl->n)
		{
			dupl = dupl->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dupl)
		return (1);
	return (0);
}

