## Flask Application Design

### HTML Files

- **index.html**:
  - Main HTML page where the map and other content will be displayed.
  - Include necessary JavaScript libraries for map functionality (e.g., Leaflet).
  - Define a div element where the map will be rendered.

### Routes

- **index**:
  - Render the `index.html` page as a response.

- **air_quality_data**:
  - API endpoint that handles fetching and preparing the air quality data to be displayed on the map.
  - Can be implemented as a function-based view or a class-based view.
  - Return the data as a JSON response.

- **static/:
  - Route to serve static files (e.g., CSS, JS, images) used by the application.

### Usage

1. The `index.html` page will load the Leaflet map and make an AJAX request to the `air_quality_data` endpoint.
2. The `air_quality_data` endpoint will fetch the air quality data and return it as a JSON response.
3. The `index.html` page will then use the data to overlay air quality markers on the map.