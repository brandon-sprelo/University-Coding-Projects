#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(dplyr)
library(ggvis) 
setwd("~/Desktop/stat133/stat133-hws-fall17/hw04/code")
source("functions.R")

categorical <- c('HW1', 'HW2','HW3', 'HW4', 'HW5', 'HW6', 'HW7', 'HW8', 'HW9')

con <- c('Test1', 'Test2', "Overall")

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Grade Visualization"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
      
        #condition panel for tab 1
       conditionalPanel(condition = "input.tabselected==1",
        "Grades Distribution\n  
        Row 1 = Grade, Row 2 = Freq, Row 3 = Prop"),

       #condition panel for tab 2
         conditionalPanel(condition = "input.tabselected==2",
                          selectInput("var2", "X-axis Variable", categorical,
                                      selected = 'HW1'),
                          sliderInput("Width", "Bin Width", 
                                      min = 0, max = 10, value = 1)),
       #condition panel for tab 3                        
        conditionalPanel(condition = "input.tabselected==3",
                         selectInput("var3", "X-axis Variable", con,
                                     selected = 'Test1'),
                         selectInput("var4", "Y-axis Variable", con,
                                     selected = "Overall"),
                         sliderInput("opacity", "Opacity",
                                     min = 0, max = 1, value = 0.1),
                         checkboxGroupInput("line", "Show line", c("none",
                                                                   "lm",
                                                                   "loess"),
                                            selected = "none"))
                                            
                          
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
        tabsetPanel(type = "tabs",
          tabPanel(
            "Barchart", value = 1,
            fluidRow(
              column(width = 10,
                     tableOutput("grade_dist")),
              column(width = 10,
                   plotOutput("freqs_plot")))),
          tabPanel("Histogram", value = 2,
                   fluidRow(
                     column(width = 10,
                   ggvisOutput("histogram")),
                   column(width = 10,
                          verbatimTextOutput("summary")))),
          tabPanel("Scatterplot", value = 3,
                   fluidRow(
                     column(width = 10,
                   ggvisOutput("scatterplot")),
                   column(width = 10,
                          verbatimTextOutput("cor")))),
          id = "tabselected")
   )
  )
)


# Define server logic required to draw a histogram
server <- function(input, output) {
  
  #barplot for tab 1
  output$freqs_plot <- renderPlot({
    barplot(table(dat$Grade))
    
  })
  
  #grade, freq, prop table for tab 1
  output$grade_dist <- renderTable({
    rbind(table(dat$Grade), prop.table(as.data.frame(table(dat$Grade))$Freq))
  }) 
   
  #histogram for tab 2
   vis_histogram <- reactive({
     var2 <- prop("x", as.symbol(input$var2))
     dat %>% 
       ggvis(x = var2, fill := "grey") %>%
       layer_histograms(width = input$Width)#stroke := "white",
                       #width = input$bins)
   })
   
   #bind histogram to tab 2 
   vis_histogram %>% bind_shiny("histogram")
   
   #summary statistics for tab 2
   output$summary <- renderPrint({
     var2 <- prop("x", as.symbol(input$var2))
     print_stats(summary_stats(eval(parse(text = paste0("dat$", var2)))))
     })



  vis_point <- reactive({
    var3 <- prop("x", as.symbol(input$var3))
    var4 <- prop("y", as.symbol(input$var4))
    
    if (input$line == "none") {
    dat %>% 
      ggvis(x = var3, y = var4, fill := 'black') %>%
      layer_points(opacity := input$opacity)
   } else {
       dat %>% 
         ggvis(x = var3, y = var4, fill := 'black') %>%
         layer_points(opacity := input$opacity)  %>%
         layer_model_predictions(model = input$line)
     }
}) 
  
  vis_point %>% bind_shiny("scatterplot")
     
    
    output$cor <- renderPrint({
      var3 <- prop("x", as.symbol(input$var3))
      var4 <- prop("y", as.symbol(input$var4))
      cor(eval(parse(text = paste0("dat$", var3))), 
          eval(parse(text = paste0("dat$", var4))))
    }) 
  
}

# Run the application 
shinyApp(ui = ui, server = server)

