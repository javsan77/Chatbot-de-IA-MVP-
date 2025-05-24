FROM maven:3.9.6-eclipse-temurin-17 AS builder
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jdk-alpine
# Instalar curl para health checks
RUN apk add --no-cache curl
WORKDIR /app
COPY --from=builder /app/target/*.jar chatbot-backend.jar
EXPOSE 8080
CMD ["java", "-jar", "chatbot-backend.jar"]