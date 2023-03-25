# Instructions
In this exercise you will be writing code to help a freelancer communicate with a project manager by providing a few utility functions to quickly calculate day- and month rates, optionally with a given discount.

We first establish a few rules between the freelancer and the project manager:

The daily rate is 8 times the hourly rate;
A month has 22 billable days.
If the freelancer bills the project manager per month, there is a discount applied. This can be handy if the project manager has a fixed budget.

Discounts are modeled as fractional numbers (percentage) between 0.0 (0%, no discount) and 0.90 (90%, maximum discount).

# 1. Calculate the day rate given an hourly rate
Implement a function to calculate the day rate given an hourly rate:

dayRate(89);
    // => 712
    
The day rate does not need to be rounded or changed to a "fixed" precision.

# 2. Calculate the month rate, given an hourly rate and a discount
Implement a function to calculate the month rate, and apply a discount:

monthRate(89, 0.42);
    // => 9086
    
The discount is always passed as a number, where 42% becomes 0.42. The result must be rounded up to the nearest whole number.

# 3. Calculate the number of workdays given a budget, rate and discount
Implement a function that takes a budget, a rate per hour and a discount, and calculates how many full days of work that covers.

daysInBudget(20000, 89, 0.2002);
    // => 35
    
The discount is always passed as a number. 20.02% is passed as 0.2002. The result is the number of days should be rounded down to full days of work.


----------------------------------------------------------------------------------

# Instructions
Translate RNA sequences into proteins.

RNA can be broken into three nucleotide sequences called codons, and then translated to a polypeptide like so:

RNA: "AUGUUUUCU" => translates to

Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>

Protein: "Methionine", "Phenylalanine", "Serine"

There are 64 codons which in turn correspond to 20 amino acids; however, all of the codon sequences and resulting amino acids are not important in this exercise. If it works for one codon, the program should work for all of them. However, feel free to expand the list in the test suite to include them all.

There are also three terminating codons (also known as 'STOP' codons); if any of these codons are encountered (by the ribosome), all translation ends and the protein is terminated.

All subsequent codons after are ignored, like this:

RNA: "AUGUUUUCUUAAAUG" =>

Codons: "AUG", "UUU", "UCU", "UAA", "AUG" =>

Protein: "Methionine", "Phenylalanine", "Serine"

Note the stop codon "UAA" terminates the translation and the final methionine is not translated into the protein sequence.

Below are the codons and resulting Amino Acids needed for the exercise.

Codon	Protein
AUG	Methionine
UUU, UUC	Phenylalanine
UUA, UUG	Leucine
UCU, UCC, UCA, UCG	Serine
UAU, UAC	Tyrosine
UGU, UGC	Cysteine
UGG	Tryptophan
UAA, UAG, UGA	STOP
Learn more about protein translation on Wikipedia

If an invalid character or codon is encountered during translation, it should throw an error with the message Invalid codon.

translate('AAA');
    // => Error: Invalid codon
    