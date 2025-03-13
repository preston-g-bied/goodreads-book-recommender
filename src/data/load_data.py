"""
Data loading utilities for the GoodReads recommendation system.
"""

import os
import pandas as pd
from pathlib import Path

def get_data_path():
    """Get the path to the data directory."""
    # use environment variable if available, otherwise use default
    data_path = os.getenv('DATA_PATH', './data')
    return Path(data_path)

def load_ratings(filename='ratings.csv', data_dir=None):
    """Load the ratings data."""
    if data_dir is None:
        data_dir = get_data_path() / 'raw'
    
    file_path = Path(data_dir) / filename
    
    # check if file exists
    if not file_path.exists():
        raise FileNotFoundError(f"Ratings file not found at: {file_path}")
    
    # load the data
    print(f"Loading ratings from {file_path}")
    df = pd.read_csv(file_path)
    
    print(f"Loaded {len(df)} ratings")
    return df

def load_books(filename='books.csv', data_dir=None):
    """Load the books data."""
    if data_dir is None:
        data_dir = get_data_path() / 'raw'
    
    file_path = Path(data_dir) / filename
    
    # check if file exists
    if not file_path.exists():
        raise FileNotFoundError(f"Books file not found at: {file_path}")
    
    # load the data
    print(f"Loading books from {file_path}")
    df = pd.read_csv(file_path)
    
    print(f"Loaded {len(df)} books")
    return df

def load_to_read(filename='to_read.csv', data_dir=None):
    """Load the to-read data."""
    if data_dir is None:
        data_dir = get_data_path() / 'raw'
    
    file_path = Path(data_dir) / filename
    
    # check if file exists
    if not file_path.exists():
        raise FileNotFoundError(f"To-read file not found at: {file_path}")
    
    # load the data
    print(f"Loading to-read data from {file_path}")
    df = pd.read_csv(file_path)
    
    print(f"Loaded {len(df)} to-read entries")
    return df

def load_book_tags(filename='book_tags.csv', data_dir=None):
    """Load the book tags data."""
    if data_dir is None:
        data_dir = get_data_path() / 'raw'
    
    file_path = Path(data_dir) / filename
    
    # check if file exists
    if not file_path.exists():
        raise FileNotFoundError(f"Book tags file not found at: {file_path}")
    
    # load the data
    print(f"Loading book tags from {file_path}")
    df = pd.read_csv(file_path)
    
    print(f"Loaded {len(df)} book tag entries")
    return df

def load_tags(filename='tags.csv', data_dir=None):
    """Load the tags data."""
    if data_dir is None:
        data_dir = get_data_path() / 'raw'
    
    file_path = Path(data_dir) / filename
    
    # check if file exists
    if not file_path.exists():
        raise FileNotFoundError(f"Tags file not found at: {file_path}")
    
    # load the data
    print(f"Loading tags from {file_path}")
    df = pd.read_csv(file_path)
    
    print(f"Loaded {len(df)} tags")
    return df

def load_all_data(data_dir=None):
    """
    Load all available datasets.
    
    Returns:
    --------
    dict
        Dictionary containing all dataframes
    """
    data = {}
    
    try:
        data['ratings'] = load_ratings(data_dir=data_dir)
    except FileNotFoundError as e:
        print(e)
    
    try:
        data['books'] = load_books(data_dir=data_dir)
    except FileNotFoundError as e:
        print(e)
    
    try:
        data['to_read'] = load_to_read(data_dir=data_dir)
    except FileNotFoundError as e:
        print(e)
    
    try:
        data['book_tags'] = load_book_tags(data_dir=data_dir)
    except FileNotFoundError as e:
        print(e)
    
    try:
        data['tags'] = load_tags(data_dir=data_dir)
    except FileNotFoundError as e:
        print(e)
    
    return data

def get_data_summary(data):
    """
    Generate a summary of all loaded data.
    
    Parameters:
    -----------
    data : dict
        Dictionary containing dataframes from load_all_data()
        
    Returns:
    --------
    str
        A summary string
    """
    summary = "Dataset Summary:\n"
    
    if 'ratings' in data:
        summary += f"- Ratings: {len(data['ratings'])} entries\n"
        summary += f"  - Unique users: {data['ratings']['user_id'].nunique()}\n"
        summary += f"  - Unique books: {data['ratings']['book_id'].nunique()}\n"
        summary += f"  - Rating range: {data['ratings']['rating'].min()} to {data['ratings']['rating'].max()}\n"
    
    if 'books' in data:
        summary += f"- Books: {len(data['books'])} entries\n"
        if 'authors' in data['books'].columns:
            summary += f"  - Unique authors: {data['books']['authors'].nunique()}\n"
    
    if 'to_read' in data:
        summary += f"- To-read: {len(data['to_read'])} entries\n"
        summary += f"  - Unique users: {data['to_read']['user_id'].nunique()}\n"
        summary += f"  - Unique books: {data['to_read']['book_id'].nunique()}\n"
    
    if 'book_tags' in data:
        summary += f"- Book tags: {len(data['book_tags'])} entries\n"
        summary += f"  - Unique books: {data['book_tags']['goodreads_book_id'].nunique()}\n"
        summary += f"  - Unique tags: {data['book_tags']['tag_id'].nunique()}\n"
    
    if 'tags' in data:
        summary += f"- Tags: {len(data['tags'])} entries\n"
    
    return summary

if __name__ == "__main__":
    # test the data loading functions
    data = load_all_data()
    
    # print a summary of the loaded data
    summary = get_data_summary(data)
    print("\n" + summary)
    
    # display the first few rows of each dataset
    for name, df in data.items():
        if df is not None:
            print(f"\n{name.upper()} preview:")
            print(df.head())