#include "lists.h"

/**
 * reverselist - reverse linked list
 * @head: head of linked list
 * Return: linked list
 */
listint_t *reverselist(listint_t *head)
{
	if (head->next == NULL)
		return (head);
	return (reverselist(head->next)->head);
}
/**
 * is_palindrome - check if a linked list is palindrome
 * @head: pointer to the head of a linked list
 * Retrun: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *reverse = reverselist(*head)
}
