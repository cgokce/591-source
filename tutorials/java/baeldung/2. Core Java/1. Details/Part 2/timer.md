#### Timer Basics

    https://www.baeldung.com/java-timer-and-timertask

- Java Classes used to schedule tasks in a background thread
    - TimerTask: Task to perform
    - Timer Scheduler

Schedule a Task Once
- After a Given Delay, given as second parameter

        @Test
        public void givenUsingTimer_whenSchedulingTaskOnce_thenCorrect(){
            TimerTask task = new TimerTask() {
                public void run() {
                    System.out.println("Task Performed on: " + new Date() + "n" +
                        "Thread's name: " + Thread.currentThread().getName());
                    )
                }
            }
            
            Timer timer = new Timer("Timer");
            
            long delay = 1000L;
            timer.schedule(task, delay);
        }

- At a given Date and Time

        Date twoSecondsLaterAsDate = Date.from(twoSecondsLater.atZone(ZoneId.systemDefault()).toInstant());
        new Timer().schedule(new DatabaseMigrationTask(oldDatabase, newDatabase), twoSecondsLaterAsDate)


Schedule a Repeatable Task
- We can schedule a repetition to observe either a fixed delay or a fixed rate
    - Fixed delay: Execution will start a period of time after the moment last execution started
    - Fixed Rate: Each execution will respect the initial schedule no mater if prev execution started
- I'll omit the details, unnecessary in most cases

Cancel Timer and Timer Task
- Execution of a task can be cancelled in many ways
    - TimerTask.cancel() method inside run() method's implementation in Timer Task itsekf
    - By calling Timer.cancel() method on Timer object
    - Stop the thread inside the run method

---

ExecutorService
- You can also use ExecutorService to schedule timer tasks

        TimerTask repeatedTask = new TimerTask() {
            public void run {...}
        };

        ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();
        executor.scheduleAtFixedRate(repeatedTaks, delay, period, TimeUnit.MILISECONDS);
        ...
        executor.shutdown();

- Comparison with timer
    - Timer can be sensitive to changes in system clock, executor is not
    - Timer has only one execution thread, executor can be configured
    - Runtime exceptions thrown inside timerTask kill the thread, executor only cancels the current task

Quartz Job Scheduler
- If you need more complete and complex solutions use a library, eg. Quartz Job Scheduler Library