"""
Addis Ababa Climate Analysis - LOAD FROM CSV FILES ONLY
Simple and direct - no API calls
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ============================================
# LOAD DATA FROM CSV FILES
# ============================================

def load_from_csv():
    """Load data directly from CSV files you already saved"""
    
    print("="*60)
    print("📂 LOADING DATA FROM CSV FILES")
    print("="*60)
    
    # Your CSV files
    hourly_file = 'addis_weather_1950_2024_hourly.csv'
    daily_file = 'addis_weather_1950_2024_daily.csv'
    
    # Check if files exist
    import os
    if not os.path.exists(hourly_file):
        print(f"\n❌ ERROR: {hourly_file} not found!")
        print("   Please make sure you saved the data first.")
        return None, None
    
    # Load hourly data
    print(f"\n📖 Loading {hourly_file}...")
    hourly_df = pd.read_csv(hourly_file, index_col=0, parse_dates=True)
    print(f"   ✓ Loaded {len(hourly_df):,} hourly records")
    
    # Load daily data
    print(f"📖 Loading {daily_file}...")
    daily_df = pd.read_csv(daily_file, index_col=0, parse_dates=True)
    print(f"   ✓ Loaded {len(daily_df):,} daily records")
    
    # Display info
    print(f"\n📅 Date range: {hourly_df.index[0].date()} to {hourly_df.index[-1].date()}")
    print(f"   Total years: {hourly_df.index[-1].year - hourly_df.index[0].year + 1}")
    
    return hourly_df, daily_df

# ============================================
# ANALYSIS
# ============================================

def analyze_data(hourly_df, daily_df):
    """Analyze the climate data"""
    
    print("\n" + "="*60)
    print("📊 CLIMATE ANALYSIS")
    print("="*60)
    
    results = {}
    
    # Basic statistics
    print("\n📍 CLIMATE STATISTICS:")
    print("-" * 40)
    
    results['mean_temp'] = hourly_df['temperature_2m'].mean()
    results['max_temp'] = hourly_df['temperature_2m'].max()
    results['min_temp'] = hourly_df['temperature_2m'].min()
    results['total_rainfall'] = daily_df['rain_sum'].sum()
    
    print(f"Average Temperature: {results['mean_temp']:.1f}°C")
    print(f"Record High: {results['max_temp']:.1f}°C")
    print(f"Record Low: {results['min_temp']:.1f}°C")
    print(f"Total Rainfall: {results['total_rainfall']:.0f} mm")
    
    # Yearly trends
    hourly_df['year'] = hourly_df.index.year
    yearly_temp = hourly_df.groupby('year')['temperature_2m'].mean()
    yearly_rain = daily_df.groupby(daily_df.index.year)['rain_sum'].sum()
    
    # Temperature trend
    first_year = yearly_temp.index[0]
    last_year = yearly_temp.index[-1]
    temp_change = yearly_temp.iloc[-1] - yearly_temp.iloc[0]
    
    print(f"\n📈 TEMPERATURE TREND:")
    print(f"   {first_year}: {yearly_temp.iloc[0]:.1f}°C")
    print(f"   {last_year}: {yearly_temp.iloc[-1]:.1f}°C")
    print(f"   Change: {temp_change:+.2f}°C")
    
    # Calculate warming rate per decade
    years_span = last_year - first_year
    warming_per_decade = (temp_change / years_span) * 10
    print(f"   Warming rate: {warming_per_decade:.2f}°C per decade")
    
    results['yearly_temp'] = yearly_temp
    results['yearly_rain'] = yearly_rain
    results['temp_change'] = temp_change
    results['warming_rate'] = warming_per_decade
    
    return results

# ============================================
# VISUALIZATIONS
# ============================================

def create_visualizations(hourly_df, daily_df, results):
    """Create visualizations from data"""
    
    print("\n🎨 Creating visualizations...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Temperature trend
    ax1 = axes[0, 0]
    ax1.plot(results['yearly_temp'].index, results['yearly_temp'].values, 
             'o-', linewidth=2, markersize=4, color='red', alpha=0.7)
    ax1.set_title(f'Temperature Trend (Warming: {results["temp_change"]:+.1f}°C)', 
                  fontweight='bold')
    ax1.set_ylabel('Temperature (°C)')
    ax1.set_xlabel('Year')
    ax1.grid(True, alpha=0.3)
    
    # 2. Rainfall trend
    ax2 = axes[0, 1]
    ax2.bar(results['yearly_rain'].index, results['yearly_rain'].values, 
            color='steelblue', alpha=0.7, width=0.8)
    ax2.set_title('Annual Rainfall', fontweight='bold')
    ax2.set_ylabel('Rainfall (mm)')
    ax2.set_xlabel('Year')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # 3. Monthly patterns
    ax3 = axes[1, 0]
    hourly_df['month'] = hourly_df.index.month
    monthly_temp = hourly_df.groupby('month')['temperature_2m'].mean()
    monthly_rain = daily_df.groupby(daily_df.index.month)['rain_sum'].mean()
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    ax3.bar(months, monthly_temp.values, color='coral', alpha=0.7)
    ax3.set_title('Average Monthly Temperature', fontweight='bold')
    ax3.set_ylabel('Temperature (°C)')
    ax3.tick_params(axis='x', rotation=45)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # 4. Temperature distribution
    ax4 = axes[1, 1]
    ax4.hist(hourly_df['temperature_2m'], bins=40, color='skyblue', 
             edgecolor='black', alpha=0.7)
    ax4.axvline(results['mean_temp'], color='red', linewidth=2, 
                label=f'Mean: {results["mean_temp"]:.1f}°C')
    ax4.set_title(f'Temperature Distribution ({len(hourly_df):,} observations)', 
                  fontweight='bold')
    ax4.set_xlabel('Temperature (°C)')
    ax4.set_ylabel('Frequency')
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle(f'Addis Ababa Climate Analysis ({hourly_df.index[0].year}-{hourly_df.index[-1].year})', 
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('addis_climate_analysis.png', dpi=300, bbox_inches='tight')
    print("📸 Saved: addis_climate_analysis.png")
    plt.show()

# ============================================
# MAIN
# ============================================

def main():
    """Main function - just load CSV and analyze"""
    
    print("="*60)
    print("🌍 ADDIS ABABA CLIMATE ANALYSIS")
    print("="*60)
    
    # Load from CSV files
    hourly_df, daily_df = load_from_csv()
    
    if hourly_df is None:
        return
    
    # Analyze
    results = analyze_data(hourly_df, daily_df)
    
    # Visualize
    create_visualizations(hourly_df, daily_df, results)
    
    print("\n" + "="*60)
    print("✅ ANALYSIS COMPLETE!")
    print("="*60)

# ============================================
# RUN IT
# ============================================

if __name__ == "__main__":
    main()