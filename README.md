# compatibility-predictor

DataHouse would like to add new members to its team. To help assess candidates, this program gives each applicant a compatibily score between 0 and 1 (0 indicating the lowest possible compatibility and 1 indicating the most). 

## Description

Given a list of current team members and their respective scores (1-10) for intelligence, strength, endurance, and spicy food tolerance, we would like to predict the compatibility of each applicant. Determining compabiltilty is open-ended, so I narrowed down the team's objective to this: search for applicants who would contribute something that the team currently lacks. When an applicant ranks higher than the team average for a given attribute, their overall compatibility score increases.

We first find compatibility scores for each attribute separately. To do this we find the difference between the applicant's score and the team's average score for that attribute. The compailtiblty score is a function of this difference. The applicant's total compability score depends on the compatibility score for each attribute, with weight given to intelligence (as we prioritize intelligence more than the other attributes)

## Getting Started

### Dependencies

Input must be in JSON

## Notes & Room For Improvement



## Author

John Harrison Plhak

