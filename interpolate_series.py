# Create a function we'll use to interpolate and plot
def interpolate_and_plot(series, interpolation):

    # Create a boolean mask for missing values
    missing_values = series.isna()

    # Interpolate the missing values
    series_interp = series.interpolate(interpolation)

    # Plot the results, highlighting the interpolated values in black
    fig, ax = plt.subplots(figsize=(10, 5))
    series_interp.plot(color='k', alpha=.6, ax=ax, legend=False)
    
    # Now plot the interpolated values on top in red
    series_interp[missing_values].plot(ax=ax, color='r', lw=3, legend=False)
    plt.show()
