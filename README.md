# compatibility-predictor

DataHouse would like to add new members to its team. To help assess candidates, this program gives each applicant a compatibility score ranging from 0 to 1

## Description

Input: JSON Object containing each team member and applicant's score [1-10] for intelligence, strength, endurance, and spice tolerance.
Output: JSON Object containing each applicant's compatibility score [0-1] 

Given a list of current team members and their respective scores from 1 to 10 for intelligence, strength, endurance, and spicy food tolerance, we would like to produce a compatibility score for each applicant. The compatibility score ranges from 0 to 1, 0 indicating the lowest possible compatibility and 1 indicating the most. "Compabiltilty" is ambiguous, so I narrowed down the team's objective to this: search for applicants who would contribute something that the team currently lacks. When an applicant ranks higher than the team average for a given attribute, their overall compatibility score increases.

We first find compatibility scores for each attribute separately. To do this, we first find the difference between the applicant's score and the team's average score for that attribute. The compatibility score is a function of this difference. The applicant's total compatibility score depends on the compatibility score for each attribute, with more weight given to intelligence (as we prioritize intelligence more than the other attributes)

## Notes & Room For Improvement

To calculate an applicant's compatibility for a given attribute, we find diff, the difference between the applicant's attribute score and the team average attribute score. If diff is negative, the compatibility score for that attribute is 0. Otherwise the compatibility score is then given by: (diff * 0.21097) / (1 + 0.1 * diff)

This function is somewhat arbitrary and can be changed depending on the needs of the team. When calculating the total compatibility score for an applicant, I chose to weight intelligence twice as much the other attributes. This can also be modified depending on the team's needs.



## Author

John Harrison Plhak

