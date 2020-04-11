#include <stdio.h>

int main (void)
{
   printf("We start by initializing var to 10, and create a pointer to it called pvar\n\n");

   int var = 10;
   int* pvar = &var;

   printf("The value of var is: %d\n", var);
   printf("The address of var is: %p\n\n", &var);

   printf("pvar points to: %p\n", pvar+1);
   printf("the address of pvar is: %p\n", &pvar);
   printf("The value it ultimately derefences is: %d\n\n", *pvar);


   printf("pvar will now dereference the value in the address it points to with *pvar = 12:\n\n");
   *pvar = 12;

   printf("The value of var is now: %d\n", var);
   printf("The address of var is still: %p\n\n", &var);

   printf("pvar still points to: %p\n", pvar);
   printf("the address of pvar is still: %p\n", &pvar);
   printf("The value it now ultimately deferences is: %d\n\n", *pvar);

   printf("Lets mix things up. First lets declare a newvar to 14, and make newpointer = &newvar, and then create a pointer to pvar: \n\n");

   int newvar = 14;
   int *newpointer = &newvar;
   int **pofpvar = &pvar;

   printf("Lets check the initial information regarding the new pointer to pvar: pofvar\n\n");

   printf("the address of pofpvar is: %p\n", &pofpvar);
   printf("pofpvar points to: %p\n", pofpvar);
   printf("The address it ultimately dereferences is: %p\n\n", *pofpvar);

   printf("Now we can deference pofvar by *pofpvar = newpointer, which will make pvar point at newvar. This is the same as *pvar = newpointer: \n\n");

   *pofpvar = newpointer;


   printf("The value of var now is still: %d\n", var);
   printf("The address of var is still: %p\n\n", &var);

   printf("The value of newvar is: %d\n", newvar);
   printf("The address of newvar is: %p\n\n", &newvar);

   printf("pvar now points to: %p\n", pvar);
   printf("The value it now ultimately dereferences is: %d\n", *pvar);
   printf("The address of pvar is still: %p\n\n", &pvar);

   printf("newpointer points to: %p\n", newpointer);
   printf("The value it ultimately dereferences is: %d\n", *newpointer);
   printf("The addess of newpointer is: %p\n\n", &newpointer);

   printf("the address of pofpvar is still: %p\n", &pofpvar);
   printf("pofpvar still points to: %p\n", pofpvar);
   printf("The address it now ultimately dereferences is: %p\n\n", *pofpvar);

   printf("Note that no address changed at any point. Addresses are hardware that are set. We only change whats in addresses, be a value or another address\n\n");


}