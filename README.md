Dynamic-Programming-Linear-Space
================================

Implementation of Hirschberg's algorithm; linear space implementation of dynamic programming


The factor limits dynamic programing's application often is not running time (O(nm)) 
but the quardratic space requirement, where n and m are the length of two sequence.
The Hirschberg algorithm reduces the space requirement from O(nm) to O(n) by involves 
divide and conque technique in the dynamic Programming process. Below is an 
implementation of [Hirschberg's algorithm](http://en.wikipedia.org/wiki/Hirschberg's_algorithm).

Requirements
=============
  1. Python version >2.7
  
  2. package: [numpy] (http://www.numpy.org/)

Example Usage
=============
To display help

    python AlignTwoStringInLinearSpace.py -h

 Below command will write the alignment of two sequences to the STDOUT 

    python AlignTwoStringInLinearSpace.py file1 file2

Send Bugs/Commnents to
======================
Zhigang Wu (zhigang.wu@email.ucr.edu)



LICENSE
=========
Copyright (c) <2013>, <Zhigang Wu>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, 
       this list of conditions and the following disclaimer.
    
    2. Redistributions in binary form must reproduce the above copyright 
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of Django nor the names of its contributors may be used
       to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

