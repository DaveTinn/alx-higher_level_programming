#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a list is palindrome
 * @head: head pointer pointing to a linked list
 *
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	int pal_list;

	if (*head == NULL)
	{
		return (NULL);
	}
	while (*head != NULL)
	{
		pal_list = head->next;
		head = pal_list;
	}
	return (pal_list);
}
