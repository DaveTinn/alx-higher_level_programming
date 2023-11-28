#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list to be checked
 *
 * Return: 0 if there is no cycle, else return 1
 */
int check_cycle(listint_t *list)
{
	listint_t *cycle, *no_cycle;

	cycle = list->next;
	no_cycle = list->next->next;
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	while (no_cycle != NULL && no_cycle->next != NULL)
	{
		if (cycle == no_cycle)
		{
			return (1);
		}
		cycle = cycle->next;
		no_cycle = no_cycle->next->next;
	}
	return (0);
}
