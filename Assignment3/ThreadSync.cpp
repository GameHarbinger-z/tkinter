#include <iostream>
#include <pthread.h>
#include <unistd.h>
#include <vector>
#include <sys/types.h>
#include <sys/wait.h>
#include <cstring>

const int numThreads = 3;
pthread_t threadIds[numThreads];

void* threadFunction(void* arg) {
    int threadId = *static_cast<int*>(arg);
    pid_t processId = getpid();

    // Each thread will display its identity in reverse order
    std::cout << "I am thread " << processId << "." << threadId << std::endl;

    return nullptr;
}

void createThreadsInProcess() {
    int threadIdsArray[numThreads];

    for (int i = 0; i < numThreads; ++i) {
        threadIdsArray[i] = numThreads - i; // Create threads in reverse order
        if (pthread_create(&threadIds[i], nullptr, threadFunction, &threadIdsArray[i]) != 0) {
            std::cerr << "Failed to create thread: " << strerror(errno) << std::endl;
            exit(1);
        }
    }

    for (int i = numThreads - 1; i >= 0; --i) {
        pthread_join(threadIds[i], nullptr);
    }
}

int main() {
    const int numProcesses = 3;
    std::vector<pid_t> pids;

    // Forking processes in reverse order
    for (int i = numProcesses - 1; i >= 0; --i) {
        pid_t pid = fork();
        if (pid < 0) {
            std::cerr << "Fork failed!" << std::endl;
            return 1;
        }
        if (pid == 0) {
            std::cout << "Forked process PID: " << getpid() << std::endl;
            createThreadsInProcess();
            return 0;
        } else {
            pids.push_back(pid);
        }
    }

    for (pid_t pid : pids) {
        waitpid(pid, nullptr, 0);
    }

    return 0;
}

