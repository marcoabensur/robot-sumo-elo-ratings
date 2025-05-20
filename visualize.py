import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import json
import os
import argparse
from elo import read_competitions, update_ratings, update_wins_losses, foreign_robots, foreign_teams

def load_data(folder_path, rating_type):
    """Load and process all competition data"""
    all_competitions = read_competitions(folder_path)
    complete_ratings = {}
    complete_wins_and_losses = {}
    
    for year_data in all_competitions:
        year_competitions = year_data['competitions']['competition']
        for competition in year_competitions:
            matches = competition[rating_type]
            if not ('invalid' in competition and competition['invalid'] == "true"):
                complete_wins_and_losses = update_wins_losses(matches, complete_wins_and_losses)
                complete_ratings = update_ratings(matches, complete_ratings)
    
    return complete_ratings, complete_wins_and_losses

def filter_rankings(ratings, wins_losses, filter_foreign=True, min_matches=5):
    """Filter rankings based on criteria"""
    filtered_data = {}
    
    for name, elo in ratings.items():
        wins = wins_losses[name][0]
        losses = wins_losses[name][1]
        total_matches = wins + losses
        
        # Apply filters
        if filter_foreign and name in (foreign_robots + foreign_teams):
            continue
        if total_matches < min_matches:
            continue
            
        filtered_data[name] = {
            "elo": elo,
            "wins": wins,
            "losses": losses,
            "total": total_matches,
            "win_rate": wins / total_matches if total_matches > 0 else 0
        }
    
    return filtered_data

def visualize_rankings(data, title, top_n=20):
    """Create and display bar chart of rankings"""
    # Sort by ELO rating
    sorted_data = sorted(data.items(), key=lambda x: x[1]["elo"], reverse=True)
    
    # Take top N entries
    top_entries = sorted_data[:top_n]
    
    # Prepare data for plotting
    names = [entry[0] for entry in top_entries]
    elo_values = [entry[1]["elo"] for entry in top_entries]
    wins = [entry[1]["wins"] for entry in top_entries]
    losses = [entry[1]["losses"] for entry in top_entries]
    
    # Create figure with proper size
    plt.figure(figsize=(12, 8))
    
    # Create the bars
    bars = plt.bar(names, elo_values, color='skyblue')
    
    # Add win-loss info
    for i, bar in enumerate(bars):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + 20,
            f"{wins[i]}-{losses[i]}",
            ha='center',
            fontsize=8
        )
    
    # Customize plot
    plt.title(title, fontsize=16)
    plt.xlabel('Competitor', fontsize=12)
    plt.ylabel('ELO Rating', fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.tight_layout()
    
    # Add horizontal grid lines
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Ensure consistent y-axis range for easier comparison
    plt.ylim(1400, max(elo_values) + 100)
    
    return plt

def main():
    parser = argparse.ArgumentParser(description='Visualize Robot Sumo Elo Rankings')
    parser.add_argument('--folder', type=str, required=True, help='Folder path (auto/rc)')
    parser.add_argument('--type', type=str, default='robot', choices=['robot', 'team'], 
                        help='Visualization type (robot/team)')
    parser.add_argument('--top', type=int, default=20, help='Number of top entries to show')
    parser.add_argument('--include-foreign', action='store_true', help='Include foreign robots/teams')
    parser.add_argument('--min-matches', type=int, default=5, help='Minimum number of matches required')
    parser.add_argument('--save', action='store_true', help='Save the visualization to a file')
    args = parser.parse_args()

    # Choose the appropriate rating type
    rating_type = 'matches-robots' if args.type == 'robot' else 'matches'
    
    # Load data
    ratings, wins_losses = load_data(args.folder, rating_type)
    
    # Filter data
    filtered_data = filter_rankings(
        ratings, 
        wins_losses, 
        filter_foreign=not args.include_foreign,
        min_matches=args.min_matches
    )
    
    # Create title
    category = 'Autonomous' if args.folder.lower() == 'auto' else 'Radio-Controlled'
    entity_type = 'Robots' if args.type == 'robot' else 'Teams'
    title = f'Top {args.top} {category} {entity_type} - ELO Rankings'
    
    # Visualize data
    plt_obj = visualize_rankings(filtered_data, title, top_n=args.top)
    
    # Save or show
    if args.save:
        filename = f"{args.folder}_{args.type}_rankings.png"
        plt_obj.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Visualization saved as {filename}")
    else:
        plt_obj.show()

if __name__ == '__main__':
    main()