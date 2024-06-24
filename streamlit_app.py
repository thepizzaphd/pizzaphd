import streamlit as st
from PIL import Image
import pandas as pd

# Function to display the About Me page
def about_me():
    st.title('About Me')
    st.write("""
        Hello! I'm The Pizza PHD. I explore pizza restaurants and provide honest and comprehensive reviews with my proprietary ranking system. I want to help people discern between hype, crafty ads and sponsorships and the genuine goods. 
        My goal is to share my love for pizza and the places that I think are worth going back to.
        
        I have over three decades of experience eating pizza across the globe and currently reside in NYC where most of my reviews will be focused.
    """)

# Function to display the main page, which is now the Reviews page
# Function to display the Reviews page
def reviews_page():
    st.title('Reviews - The Good Places')
    st.subheader('Razza 06/23/2024')
    # Display an image
    review_image = Image.open('images/razza.png')
    st.image(review_image, caption='Di Natale Pizza from Razza')
    
    st.write("""
In 2017, I was first drawn to Razza by Pete Well's question in the New York Times, "Is New York’s Best Pizza in New Jersey?" Razza is the best in the world. Dan Richer doesn't follow the crowd. He takes more care than anyone else in sourcing the best ingredients whether it's local, imported or overseas. If he can't source a high quality ingredient it may stay off the menu for months. Dan doesn’t import all of his ingredients from a particular region in Italy. He doesn’t use all local ingredients. He celebrates the best ingredients which may be from Italy, California, local, or upstate. He uses a scientific way of rating ingredients that results in something completely original, not trying to be anything other than itself.   

All the ingredients harmonize and come together in a balanced way. The pizza is thin and cooked in a wood fire oven and resembles a Neapolitan Pizza but doesn’t the dough is entirely original. It’s not made with 00 flour, it’s not droopy (this isn’t a bad or good thing). The leoparding is beautiful and shows what you can do with a real wood fire oven and stops short of “New Haven Char”. 

While I rank the closest thing to a cheese or margherita pizza, It’s hard to go wrong with any of their pizzas with toppings. Standouts include: Di Natale which is an uncommon combination of garlic, raisins, pine nuts, pepperoni that may ruin other pepperoni spots for you as you discover what excellent pepperoni. You won’t find a common bella mushroom on the funghi pizza, instead you’ll get well prepared seasonal mushrooms that could turn a jaded mushroom eater into a fan of mushrooms.

Other notable non-pizza dishes include bread and butter and meatballs. The dough is probably the most important aspect of a pizza and Dan has definitely mastered dough for pizza and loaves of bread. Bread and butter isn’t free here but it’s superb with beautiful deep yellow butter. The meatball dish showcases the wonderful tomatoes used at Razza and gives a generous side of sauce that you may dip bread or crusts into. While I prefer my meatballs to have more meat and a chew to them, Razza seems to incorporate more bread and water which makes them softer. You may also ask for chili oil which is reminiscent of calabrian chili but appears to be another variety of pepper. 

Almost a decade ago there was a cult following, you put your name down and waited a couple of hours like Lucali. Razza could have been snotty with its cult following but instead they transformed the experience for the customer for the better. Today, you can conveniently make a Resy or order takeout online. When you arrive, you’re greeted by multiple staff and there’s plenty of outdoor seating. It’s no wonder they were named the best pizza in North America in 2019. A trip on the PATH for locals or visitors is time well spent. You’ll walk away with the genuine goods, pizza that is unsurpassed and inimitable and a place you’ll be happy to return to. 
    """)
    
    # Load the pizza rankings data, setting the second row as the header
    pizza_rankings = pd.read_csv('data/pizza_rankings.csv', header=1)  # This skips the first row and uses the second row as headers
    
    # Load the pizza rankings data, setting the second row as the header
    pizza_rankings = pd.read_csv('data/pizza_rankings.csv', header=1)  # This skips the first row and uses the second row as headers

    # Correct the column names due to spelling errors and display only the specified columns
    selected_columns = pizza_rankings[['Just The Pizza - Adjusted Score out of 100', 'Overall Expereince - Adjusted Score out of 100', 'Adjusted score out of 100']]
    
    # Display the filtered DataFrame
    st.dataframe(selected_columns)
 # Filter the DataFrame for the restaurant 'Razza'
    razza_data = pizza_rankings[pizza_rankings['Restaurant'] == 'Razza']
    st.dataframe(razza_data)

# Function to display the Scoring Methodology page with FAQs
def scoring_methodology():
    st.title('Scoring Methodology')
    st.write("""
        Explanation of scoring system...
    """)
    
    st.header('FAQs')
    st.write("""
        **Q: How are scores calculated?**
        A: Scores are calculated based on several criteria...

        **Q: What makes a good score?**
        A: A good score is derived from...
    """)

# Add a sidebar for navigation
page = st.sidebar.selectbox('Choose a page:', ['Reviews - The Good Places', 'About Me', 'Scoring Methodology'])

# Display the selected page
if page == 'Reviews - The Good Places':
    reviews_page()
elif page == 'About Me':
    about_me()
elif page == 'Scoring Methodology':
    scoring_methodology()
