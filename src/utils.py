import seaborn as sns

def configure_seaborn_settings():
    # Brown and blue color palette using a diverging palette
    sns.set_palette(sns.color_palette(sns.diverging_palette(250, 30, l=65, center="dark")))
    
    # Set the context to 'notebook' which is suitable for Jupyter Notebooks
    sns.set_context('notebook')
    
    # Set the style to 'darkgrid' for dark background with grid lines
    sns.set_style('darkgrid')

