#include <iostream>
#include <pthread.h>
#include <unistd.h>
#include <sys/wait.h>

using namespace std;

void* threadAction(void* id){
	int threadId = *static_cast<int*>(id);
	printf("\nThis is thread %d.%d\n", getpid(), threadId);
	pthread_exit(NULL);
}

int main(int argc, char *argv[]){
	int p1, p2, p3;
	p1 = fork();
	p2 = fork();
	p3 = fork();
	if(p1 == 0){
		pthread_t threads[3];
		int threadIds[3];
		printf("This is process %d\n", getpid());
		for(int t = 0; t < 3; t++){
			threadIds[t] = t+1;
			pthread_create(&threads[t], NULL, threadAction, &threadIds[t]);
	}
	}else{
		waitpid(p1, NULL, 0);
	}
	if(p2 ==0){
		pthread_t threads[3];
		int threadIds[3];
		printf("This is process %d\n", getpid());
		for(int t = 0; t < 3; t++){
			threadIds[t] = t+1;
			pthread_create(&threads[t], NULL, threadAction, &threadIds[t]);
		}
	}else{
		waitpid(p2, NULL, 0);
	}
	if(p3 == 0){
		pthread_t threads[3];
		int threadIds[3];
		printf("This is process %d\n", getpid());		
		for(int t = 0; t < 3; t++){
			threadIds[t] = t+1;
			pthread_create(&threads[t], NULL, threadAction, &threadIds[t]);
		}
	}else{
		waitpid(p3, NULL, 0);
	}
	return 1;
}
