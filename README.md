# p8105_final_musicndrug

1206/readme
```{r} 
genly_billboard %>%
  ggplot(aes(x = year, y = 100 * p_lyrics, color = lyr_des)) +
    geom_point() +
    geom_smooth(aes(group = lyr_des), se = F) +
    labs(title = "substance description(%) from 1999 to 2019",
         y = "substance mentioned(%)",
         color = "substance")
```
songs_abuse%>%
  filter(stname=="National", outcome=="Marijuana use in the past month",description=="marijuana")%>%
  group_by(year)%>%
  ggplot(aes(x = p_lyrics, y = bsae, color = agegrp)) +
    geom_point() +
    geom_smooth(aes(group = agegrp), se = F) +
   labs(title = "Marijuana use Vs % of marijuana lyric national level",
         y = "Marijuana use in the past(%)",
         color = "agegroup")
         
 Recode_abuse
 songs_abuse%>%
   filter(outcome=="Marijuana use in the past month
",area==0)%>%
  group_by(agegrp)%>%
  summarize(
  mean_bsae = mean(bsae)
)%>%
  ggplot(x = year, y = mean_bsae) +
  geom_point(aes(color = agegrp), alpha = .5)
