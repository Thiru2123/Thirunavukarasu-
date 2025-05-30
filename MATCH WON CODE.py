p_matches_won <- tbl_ipl_data %>% filter(!is.na(winner)) %>% 
  count(winner, sort = TRUE) %>%
  top_n(n = 5, wt = n) %>% 
  ggplot() + 
  geom_col(mapping = aes(x = n, 
                         y = reorder(winner, n), 
                         fill = winner), show.legend = FALSE) + 
  geom_text(mapping = aes(x = n, 
                          y = reorder(winner, n), 
                          label = n, fontface = "bold"), 
            show.legend = FALSE, 
            color = "white", 
            size = 3, 
            hjust = "top") + 
  scale_fill_brewer(palette = "Paired") + 
  theme_solarized_2(light = FALSE, base_size = 14) + 
  theme(axis.text.x = element_text(color = "white"), 
        axis.text.y = element_text(color = "white"),
        axis.title.x = element_text(color = "white"),
        axis.title.y = element_text(color = "white"), 
        plot.title = element_text(color = "white"),
        strip.text = element_text(color = "white"),
        legend.text = element_text(color = "white"), 
        legend.title = element_text(color = "white"), 
        legend.position = "top") +
  labs(x = "Matches Won", 
       y = "")
