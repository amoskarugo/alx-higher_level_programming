#include "lists.h"
/**
 *check_cycle - a function that checks whether a singly
 *		linked list is circular or not.
 *@list: linked list passed to the function
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (1)
	{
		temp = temp->next;

		if (temp == NULL)
			return (0);
		if (temp == list)
			return (1);
	}
}
