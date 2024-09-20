# frontend/unity_project/Dockerfile

FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y wget unzip xvfb libgtk-3-0 libgbm-dev

# Install Unity dependencies and Unity Editor (headless)
# Note: Unity licensing needs to be handled appropriately

# Copy Unity build
COPY build /unity_build

# Serve Unity build with Nginx
RUN apt-get install -y nginx
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
