# Literature Review

## Early Diagnosis and Intervention in Autism

The importance of early diagnosis in autism spectrum disorder has been extensively documented, though causal evidence remains limited. {cite}`dawson2010randomized` conducted one of the first randomized controlled trials of early intensive behavioral intervention, finding significant improvements in IQ and adaptive behavior. However, RCTs are challenging to implement at scale and may not reflect real-world service delivery.

Observational studies consistently find associations between earlier diagnosis and better outcomes {cite}`clark2018school`, but these correlations may reflect selection bias. Families with higher socioeconomic status, better access to healthcare, or greater developmental concerns may seek earlier diagnosis {cite}`mandell2005racial`. This confounding makes it difficult to separate the causal effect of early diagnosis from family characteristics.

## Institutional Context and Service Transitions

In many jurisdictions, responsibility for autism services transitions between agencies at specific age cutoffs. In the United States, Part C of the Individuals with Disabilities Education Act (IDEA) provides early intervention services from birth to age 3, after which children transition to Part B preschool services {cite}`idea2004`. This transition often involves:

1. **Administrative Delays**: The handover between agencies can create waitlists and service gaps
2. **Different Eligibility Criteria**: Part B may have stricter eligibility requirements
3. **Changed Service Models**: From family-centered (Part C) to education-focused (Part B) approaches

These institutional features create plausibly exogenous variation in service access and diagnostic timing that we exploit in our identification strategy.

## Regression Discontinuity in Health Services Research

Regression discontinuity designs have been increasingly used to evaluate health interventions where randomization is infeasible {cite}`moscoe2015regression`. In autism research, {cite}`doshi2017effect` used age cutoffs in insurance coverage to estimate the impact of behavioral therapy. Our study extends this approach to examine diagnostic timing itself.

The key identifying assumption in RD designs is that individuals cannot precisely manipulate their position relative to the cutoff {cite}`lee2010regression`. In our context, parents cannot control the exact timing of when their child enters the diagnostic queue, particularly given typical waitlists of several months.

## Long-term Outcomes in Autism

Most autism intervention studies focus on short-term outcomes during childhood. Evidence on adult outcomes remains limited, though emerging research suggests substantial heterogeneity {cite}`howlin2004adult`. Employment rates for autistic adults range from 25-50%, with higher rates among those without intellectual disability {cite}`taylor2015employment`. Independent living is achieved by approximately 20-30% of autistic adults {cite}`farley2009twenty`.

The relationship between early intervention and adult outcomes has rarely been studied due to the long follow-up required. {cite}`pickles2016parent` found that early intervention effects on language persisted through adolescence, but adult outcomes were not assessed. Our study addresses this gap by examining outcomes through age 25.

## Mechanisms

Several mechanisms may explain why early diagnosis improves outcomes:

1. **Neural Plasticity**: The brain's capacity for change is greatest in early childhood {cite}`dawson2008early`
2. **Developmental Cascades**: Early skills provide foundations for later development {cite}`mundy2007joint`
3. **Family Adaptation**: Earlier diagnosis allows families more time to adjust and access resources {cite}`zwaigenbaum2015early`
4. **Educational Planning**: Early identification enables appropriate educational placement and support {cite}`harris2000age`

## Summary

While substantial literature documents associations between early diagnosis and better outcomes in autism, causal evidence remains limited. Our regression discontinuity design addresses this gap by exploiting institutional features that create quasi-random variation in diagnostic timing. By tracking outcomes through early adulthood, we provide new evidence on the long-term impacts of early identification and intervention.