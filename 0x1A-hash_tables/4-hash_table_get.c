#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "hash_tables.h"

/**
 * hash_table_get - function that retrieves a value assciated
 * with an key.
 *
 * @ht: pointer to hashtable.
 * @key: key
 *
 * Return: value, NULL if key doesn't exist.
 */

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long size = ht->size;
	unsigned long index = key_index((const unsigned char *)key, size);
	hash_node_t *nod;

	if (ht == NULL || key == NULL)
		return (0);

	nod = ht->array[index];
	while (nod != NULL)
	{
		if (strcmp(nod->key, key) == 0)
			return (nod->value);
	}
	return (NULL);
}
