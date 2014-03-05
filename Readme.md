Git Svn Keyword Replacement
===========================

Replaces the svn tags of $Log$ and $Id$ with git commit history

Sample:

Input:
```
// File: $Id$

#include <stdio>

int main() {
	printf("Some code")
}

// $Log$ 
```

Output:
```
// File: $Id: a6b09a3 Code complete. Now ignores hidden files $

#include <stdio>

int main() {
	printf("Some code")
}

// $Log: $ 
// commit a6b09a36f66f0959d0972da279736bcfabc845c9
// Author: Mike Lyons <mdl0394@gmail.com>
// Date:   Wed Mar 5 00:30:10 2014 -0500
// 
//     Code complete. Now ignores hidden files
// 
// commit 7df42e9e538bd8f425ccdbf910ce73e8cd1178ee
// Author: Mike Lyons <mdl0394@gmail.com>
// Date:   Wed Mar 5 00:13:58 2014 -0500
// 
//     Code worked on. Added more content to test file
// 
// commit b7f00ec7220c7ddd80a50c6ecfe23c3891e1dfbc
// Author: Mike Lyons <mdl0394@gmail.com>
// Date:   Tue Mar 4 12:37:08 2014 -0500
// 
//     Added Test File
// 
```
