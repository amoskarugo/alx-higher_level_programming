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


#endif
