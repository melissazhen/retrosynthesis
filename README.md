# retrosynthesis

This repository contains the following work:

1. enables the retrosim (https://github.com/connorcoley/retrosim) written in Python 2.7 to run in Python 3.10;

2. gives two ways of atommaping, the indigo and the RXNMapper (https://github.com/rxn4chemistry/rxnmapper);

3. constructs a new retrosynthesis model using the open-source RDChiral wrapper for RDKit (https://github.com/connorcoley/rdchiral) 
   and presents its top-n accurary training on data_processed_USPTO acquired from retrosim      (https://github.com/connorcoley/retrosim/blob/master/retrosim/data/data_processed.csv);

4. provides the data on explosives reactions collected from Reaxys (mainly) and other scientific literatures. The name of corresponding explosives is also provided to enable that we can add more explosive reactions about other explosives later.

5. uses the new retrosynthesis model to propose and rank candidate precursors and shows top-n accuracy, using data_processed_USPTO, data_processed_reaxys, data_processed_USPTO + reaxys as training datasets.
