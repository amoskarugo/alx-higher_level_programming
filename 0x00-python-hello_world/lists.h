#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 *struct node - a linked list structure
 *@n: variable to store data
 *@next: pointer to the next node
 */
typedef struct node
{
	int n;
	struct node *next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
#endif
