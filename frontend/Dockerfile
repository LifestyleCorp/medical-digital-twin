# Use official Node.js image as base
FROM node:14

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json ./
RUN npm install

# Copy project files
COPY . .

# Build the app
RUN npm run build

# Serve the app with a simple server (optional)
# You can use nginx or any other server
# For simplicity, we'll use serve
RUN npm install -g serve

# Expose port
EXPOSE 3000

# Start the app
CMD ["serve", "-s", "build", "-l", "3000"]
