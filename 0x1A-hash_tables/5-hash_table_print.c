#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "hash_tables.h"

/**
 * hash_table_print - functiion that prints a hash table.
 * @ht: hash function.
 */
void hash_table_print(const hash_table_t *ht)
{
	hash_node_t *nod;
	unsigned long int cont = 0, i = 0;

	if (ht != NULL)
	{
		printf("{");
		for (cont = 0; cont < ht->size; cont++)
		{
			nod = ht->array[cont];
			while (nod != NULL)
			{
				if (i != 0)
				{
					printf(", ");
					i = 1;
					printf("'%s': '%s'", nod->key, nod->value);
					nod = nod->next;
				}
			}
		}
		printf("}\n");
	}
}
