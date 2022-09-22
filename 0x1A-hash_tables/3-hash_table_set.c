#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "hash_tables.h"

/**
 *hash_table_set - adds an element to the hash table
 *@ht: pointer to the hash
 *@key: pointer to the key
 *@value: value to add
 *Return: 1 if is success or 0
 */

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long size = ht->size;
	unsigned long index = key_index((const unsigned char *)key, size);
	hash_node_t *newNode;

	if (ht == NULL || key == NULL || value == NULL)
		return (0);

	if (ht->array[index] != NULL && strcmp(ht->array[index]->key, key) == 0)
	{
		ht->array[index]->value = strdup(value);
		return (1);
	}

	newNode = malloc(sizeof(hash_node_t));

	if (new_node == NULL)
		return (0);

	newNode->key = strdup(key);
	newNode->value = strdup(value);
	newNode->next = ht->array[index];
	ht->array[index] = newNode;
	return (1);
}
