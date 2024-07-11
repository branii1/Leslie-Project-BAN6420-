# Load the R6 package to create classes in R
library(R6)

# Define a simple Worker class
Worker <- R6Class("Worker",
  public = list(
    worker_id = NULL,
    name = NULL,
    gender = NULL,
    salary = NULL,
    level = NULL,
    
    initialize = function(worker_id, name, gender, salary) {
      self$worker_id <- worker_id
      self$name <- name
      self$gender <- gender
      self$salary <- salary
      self$level <- self$assign_level()
    },
    
    # Method to assign employee level based on salary and gender
    assign_level = function() {
      tryCatch({
        if (self$salary > 10000 & self$salary < 20000) {
          return("A1")
        } else if (self$salary > 7500 & self$salary < 30000 & tolower(self$gender) == "female") {
          return("A5-F")
        } else {
          return("Unknown")
        }
      }, error = function(e) {
        message(sprintf("Error in assigning level for worker %d: %s", self$worker_id, e$message))
        return("Error")
      })
    },
    
    # Method to generate payment slip for the worker
    generate_payment_slip = function() {
      tryCatch({
        slip <- sprintf("Payment Slip for %s (ID: %d):\n", self$name, self$worker_id)
        slip <- paste0(slip, sprintf("Gender: %s\n", self$gender))
        slip <- paste0(slip, sprintf("Salary: $%.2f\n", self$salary))
        slip <- paste0(slip, sprintf("Employee Level: %s\n", self$level))
        return(slip)
      }, error = function(e) {
        message(sprintf("Error in generating payment slip for worker %d: %s", self$worker_id, e$message))
        return("Error generating payment slip")
      })
    }
  )
)

# Function to create a list of workers dynamically
create_workers <- function(num_workers = 400) {
  workers <- list()
  names <- c("Kwadwo", "Kwabena", "Abena", "Nana", "Yaa", "Akosua", "Obeng", "Kwasi", "Esi", "Kwaku")
  for (i in 1:num_workers) {
    name <- sample(names, 1)
    gender <- sample(c("Male", "Female"), 1)
    salary <- sample(5000:35000, 1)
    worker <- Worker$new(worker_id = i, name = name, gender = gender, salary = salary)
    workers[[i]] <- worker
  }
  return(workers)
}

# Main function to create workers and generate payment slips
main <- function() {
  workers <- create_workers()
  for (worker in workers) {
    cat(worker$generate_payment_slip(), "\n\n")
  }
}

# Run the main function
main()
