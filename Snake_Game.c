#include <stdio.h>
#include <Windows.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#define LEFT 75
#define RIGHT 77
#define UP 72
#define DOWN 80
#pragma warning ( disable : 4996 )

typedef struct pos
{
    int x, y;
}POS;

void gotoxy(int x, int y, char* s)
{
    COORD Pos = { x * 2,y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Pos);
    printf("%s", s);
}

void draw_screen()  ///처음 맵 테두리 그리기
{
    int i;

    system("cls");

    gotoxy(0, 0, "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■");

    for (i = 1; i < 20; i++)
    {

        gotoxy(0, i, "■");

        gotoxy(30, i, "■");

    }
    gotoxy(0, 20, "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n");
}

int check(POS* snake, int len)//0은 게임 오버, 1은 계속 실행 (뱀 충돌 실험)
{
    int i;
    if (snake[0].x == 0 || snake[0].x == 20 || snake[0].y == 0 || snake[0].y == 30) {
        return 0;
    }
    for (i = 1; i < len; i++) {
        if (snake[0].x == snake[i].x && snake[0].y == snake[i].y) return 0;
    }
    return 1;
}

void move(POS* snake, int len)
{
    static int dir = -1;
    int key, i;
    if (kbhit() == 1) {
        do
        {
            key = getch();
        } while (key == 224);
        switch (key)
        {
        case LEFT:
            dir = 0;
            break;
        case RIGHT:
            dir = 1;
            break;
        case UP:
            dir = 2;
            break;
        case DOWN:
            dir = 3;
            break;
        }
    }

    if (dir != -1) {
        gotoxy(snake[len - 1].y, snake[len - 1].x, "  ");
        for (i = len - 1; i > 0; i--) {
            snake[i] = snake[i - 1];
        }
        gotoxy(snake[1].y, snake[1].x, "○");
    }

    if (dir != -1) {
        switch (dir)
        {
        case 0:
            snake[0].y--;
            break;
        case 1:
            snake[0].y++;
            break;
        case 2:
            snake[0].x--;
            break;
        case 3:
            snake[0].x++;
            break;
        }
    }
    gotoxy(snake[0].y, snake[0].x, "●");
}

int main()//메인함수
{
    POS snake[100], item;
    int i, speed = 150, len = 4;//뱀의 길이는 최대 100

    draw_screen();

    srand(time(NULL));

    for (i = 0; i < len; i++) {
        snake[i].x = 10;
        snake[i].y = 14 + i;
        gotoxy(snake[i].y, snake[i].x, "○");
    }
    

    item.x = rand() % 18 + 1;
    item.y = rand() % 28 + 1;
    gotoxy(item.y, item.x, "º");

    while (1)
    {
        if (check(snake, len) == 0) break; //뱀 충돌 체크함수

        if (snake[0].x == item.x && snake[0].y == item.y) {//아이템 판별
            if (speed > 20) speed -= 5;
            if (len < 100) {
                len++;
                snake[len] = snake[len - 1];
            }
            item.x = rand() % 18 + 1;
            item.y = rand() % 28 + 1;
        }
        gotoxy(item.y, item.x, "º");

        move(snake, len);//뱀 이동 함수

        Sleep(speed);
    }
    gotoxy(12, 10, "!!!GAME OVER!!!");
    return 0;
}