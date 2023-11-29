#include "lists.h"
/**
 * insert_node - inserts a node in a sorted singly linked list
 * @head: head pointer to singly linked list
 * @number: number to be inserted
 *
 * Return: NULL if failure, else address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_Node, *curr_Node, *prev_Node;

	new_Node = malloc(sizeof(listint_t));
	if (new_Node == NULL)
	{
		return (NULL);
	}
	new_Node->n = number;
	new_Node->next = NULL;
	while (curr_Node != NULL && curr_Node->n != number)
	{
		prev_Node = curr_Node;
		curr_Node = curr_Node->next;
	}
	return (new_Node);
}
