#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list to be checked
 *
 * Return: 0 if there is no cycle, else return 1
 */
int check_cycle(listint_t *list)
{
        listint_t head_Node;

        if (head_Node == NULL)
        {
                return (1);
        }
