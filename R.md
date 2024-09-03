# Data Types in R
numeric (floats)
integer (1L, 55L... L declares this as an integer)
complex (i is the imaginary part)
character (string) --> surrounded by "" or ''
logical (boolean)
fruits <- list("apple", "banana", "cherry")

# Functions
print() --> no need to use unless variable in a for loop
paste (va1,va2) --> concatenates 2 strings
class(x) --> type
cat() --> to print a multipl-line string and when using ecape characters (\\, \n, \r (carriage return), \t, \b)
nchar()--> find number of characters of a string
grepl("Char", str_var)--> checks if char is in var

### Assigning value to variable
var1 <- value
value -> var1
my_var <<- value (global assigner)
value ->> my_var

### Type conversion
var <- as.numeric(var1)
as.integer( )
as.complex( )

### Operators
`+ - * / ^ %%` (Modulus) `%/%` (Integer division)
`> == < != >= <=` --> return boolean
max(val,val,val...)
min(same)
sqrt(val)
abs()--> absolute value
ceiling(1.4)
floor(1.4)

### Conditions/Loops
if (b > a) {
  print ("b is greater than a")
} `else / else if` {
  print("b is not greater than a")
}
for (x in 1:10){}
for (x in fruits){print(x)}

    while (i<6) {
        print(i)
        i <- i + 1
        if (i ==4){
            break
        }
        if (i == 3){
            next #skips 3
        }
    }

### Logical Operators
& --> returns TRUE if both elements are TRUE
&& --> returns TRUE if both statements are TRUE
| --> returns TRUE if one of the elements is TRUE
|| --> returns TRUE if one of the statements are TRUE
! --> returns FALSE if statement is TRUE

### Miscellaneous Operators
%in% --> Find out if an element belongs to a vector
%*% --> Matrix multiplication

## Creating a Function
    my_function <- function(){
        #TODO write the block of code corresponding to this function
    }

###### Calling a function:
my_function()