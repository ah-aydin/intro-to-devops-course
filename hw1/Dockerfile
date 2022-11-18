FROM ubuntu

ARG IS_READY

# Install nginx
RUN apt-get update
RUN apt-get install nginx -y

# To be able to edit stuff if needed
RUN apt-get install vim -y

# Replace the default.conf file to point towards /content volume
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./content /content
VOLUME [ "/content" ]

# Check argument
RUN if [ "$IS_READY" = "true" ] ; then echo "We are ready" > /content/index.html ; else echo "We are not ready" > /content/index.html ; fi

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]