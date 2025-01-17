p8105 final proposal
================
Ling Guo (lg3158) Wenyi Liu (wl2779) Mingkuan Xu (mx2262) Shibei Xu
(sx2267)

<h1>
<center>
From “Hot 100” to “Pot 100”
</center>
</h1>
<h4>
<center>
The relationship between illicit drug use and billboard music chart
</center>
<h4>

## Motivation for this project

-   Illicit drug use is a major public health issue in United States.
    Previous studies showed a relationship between illicit drug use and
    pop music
    \[[1](https://pubmed.ncbi.nlm.nih.gov/30599351/),[2](https://www.tandfonline.com/doi/full/10.3109/10826084.2012.637433)\],
    indicating that pop music may have a potential encouraging effect on
    illicit drug use \[[3](https://pubmed.ncbi.nlm.nih.gov/18250243/)\].
    However, these studies are either cross-sectional, or need to be
    reproduce using more recent data.

## The intended final products

The intended final products will describe the trend of music genre,
frequency of illicit drug in the popular music, and the relationship
between popular music and illicit drug use.

## The anticipated data sources

-   Popular music data: from [Data on Songs from Billboard
    1999-2019](https://www.kaggle.com/danield2255/data-on-songs-from-billboard-19992019).
    The dataset contains the time of release, music genre, peak rank,
    and lyrics.

-   Illicit drug usage data: from [National Survey on Drug Use and
    Health (NSDUH)
    1999-2019](https://www.datafiles.samhsa.gov/dataset/national-survey-drug-use-and-health-2019-nsduh-2019-ds0001).
    The dataset is for state-level small area estimates (SAEs),
    associated confidence intervals, and other key statistics related to
    state-level, model-based estimates of certain key substance use and
    mental health outcomes.

## The planned analyses/visualizations/coding challenges

-   Planned analyses
    -   Descriptive information
        -   the trend of music genre, the frequency of illicit drug in
            the popular music
        -   the trend of age of first-time illicit drug usage,
            prevalence of different illicit drugs
    -   Analysis (methods pending; possibly linear regression)
        -   the relationship between the popularity of music genre and
            illicit drug popularity
        -   the relationship between the illicit drug description in
            music and the first-time illicit drug usage
        -   the relationship between the illicit drug description in
            music and the prevalence of illicit drug usage
-   Visualization
    -   the trends will present as line plots or [sankey
        plots](https://www.r-graph-gallery.com/sankey-diagram.html); the
        description of substance reference might use
        [wordcloud](https://www.r-graph-gallery.com/wordcloud.html).
    -   the relationships will present as scatter plot or
        [correlogram](https://www.r-graph-gallery.com/correlogram.html).
    -   since there might be a lagging effect in the association between
        substance reference in lyrics and actual substance use
        prevalence, line plots may be used.
    -   since state information is available in substance use data set,
        maps describing the association between music trend and
        state-stratified illicit drug usage might be present.
    -   Interactivity and animation could be included if necessary.
-   Coding challenges
    -   Data wrangling
        -   Need to narrow down the substances we want to know: need
            literature review
        -   Extracting substances from the lyrics: substance names
            varies
    -   Analysis and visualization
        -   Hard to determine the parameters
        -   Only summary data of illicit drug usage is available, might
            use meta-analysis
        -   Visualization could be coding intensive

## The planned timeline

We will meet weekly and have extra meetings if necessary; the planned
work would be done by Sunday 11:59 pm.

-   **Nov 8 - Nov 14** Decide project topic and data sources; complete
    the final proposal (DDL: Nov 13, 1pm); date the data
-   **Nov 15 - Nov 21** Analysis protocol; data wrangling; report
    outline; website outline
-   **Nov 22 - Nov 28** Analysis and data visualization; draft of
    report; website construction
-   **Nov 29 - Dec 5** Report revision; website revision; screencast
    (DDL: Dec 5, 4 pm)
