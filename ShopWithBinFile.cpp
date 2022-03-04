#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;
void menu(void);
struct product
{
    //char date[8];
    char name [30];
    float cost;
    int amount;
    int id;
    void print(void)
    {
        cout<<id<<"\t";
        cout<<name<<"\t";
        cout<<cost<<"\t";
        cout<<amount<<endl;
    }
};
struct Sellproduct
{
    char name[30];
    int date;
    int amount;
    int id;
    void show(void)
    {
        cout<<date<<"\t";
        cout<<name<<"\t";
        cout<<id<<"\t";
        cout<<amount<<endl;
    }
};

product p[50];
Sellproduct sp [100];
int indexsp=0;

void SetProduct(void)
{
    cout<<"Please enter number of products to Add : "<<endl;
    int num;
    cin>>num;
    product p[50];
    ofstream listproduct("ListProduct.bin",ios::out | ios::binary);
    listproduct.write(reinterpret_cast<char *>(&num),sizeof(int));
    for (int i=0;i<num;i++)
    {
        cout<<"please enter id of product :"<<endl;
        cin>>p[i].id;
        listproduct.write(reinterpret_cast<char *>(&p[i].id),sizeof(int));
        cout<<"please enter name of product :"<<endl;
        cin>>p[i].name;
        listproduct.write(reinterpret_cast<char *>(p[i].name),30*sizeof(char));
        cout<<"please enter cost of product :"<<endl;
        cin>>p[i].cost;
        listproduct.write(reinterpret_cast<char *>(&p[i].cost),sizeof(float));
        cout<<"please enter amount of product : "<<endl;
        cin>>p[i].amount;
        listproduct.write(reinterpret_cast<char *>(&p[i].amount),sizeof(int));
        cout<<"-----------------------------"<<endl;
    }
    listproduct.close();
    cout<<"Your Product were successfully added ..."<<endl;
}
void update(void)
{
    int num;
    fstream listproduct("ListProduct.bin",ios::out | ios::binary | ios::in);
    listproduct.read(reinterpret_cast<char *>(&num),sizeof(int));
    for (int i=0;i<num;i++)
    {
        listproduct.write(reinterpret_cast<char *>(&p[i].id),sizeof(int));
        listproduct.write(reinterpret_cast<char *>(p[i].name),30*sizeof(char));
        listproduct.write(reinterpret_cast<char *>(&p[i].cost),sizeof(float));
        listproduct.write(reinterpret_cast<char *>(&p[i].amount),sizeof(int));
    }
    listproduct.close();
}
void ShowProduct(void)
{
    cout<<"-----------------------------"<<endl<<endl;
    cout<<"code-----Name----Cost----Amount"<<endl<<endl;
    int n;
    fstream listproduct("ListProduct.bin",ios::in | ios::binary);
    listproduct.read(reinterpret_cast<char *>(&n),sizeof(int));
    for (int i=0;i<n;i++)
    {
        listproduct.read(reinterpret_cast<char*>(&p[i].id),sizeof(int));
        listproduct.read(reinterpret_cast<char*>(p[i].name),30*sizeof(char));
        listproduct.read(reinterpret_cast<char*>(&p[i].cost),sizeof(float));
        listproduct.read(reinterpret_cast<char*>(&p[i].amount),sizeof(int));
    }
    listproduct.close();
    for (int i=0;i<=n-1;i++)
    {
        p[i].print();
    }
    cout<<endl;
}
void Sell (void)
{

    string name;
    int id,amount,date,n,out;
    cout<<"Please enter 'name' of Product :"<<endl;
    cin>>name;
    cout<<"Please enter 'id' of Product :"<<endl;
    cin>>id;
    cout<<"Please enter the 'amount' you want :"<<endl;
    cin>>amount;
    cout<<"Please enter today's date :"<<endl;
    cin>>date;
    fstream listproduct("ListProduct.bin",ios::in | ios::binary |ios::out);
    listproduct.read(reinterpret_cast<char*>(&n),sizeof(int));
    for(int i=0;i<n;i++)
    {
        if(p[i].name == name && p[i].id == id)
        {
            p[i].amount = p[i].amount - amount;
            strcpy(sp[indexsp].name,name.c_str());
            sp[indexsp].id=id;
            sp[indexsp].amount=amount;
            sp[indexsp].date=date;
            indexsp++;
            update();
            fstream sellslist ("SellProduct.bin",ios::out | ios::binary | ios::app);
            sellslist.write(reinterpret_cast<char*>(&date),sizeof(int));
            sellslist.write(reinterpret_cast<char*>(&name),sizeof(string));
            sellslist.write(reinterpret_cast<char*>(&id),sizeof(int));
            sellslist.write(reinterpret_cast<char*>(&amount),sizeof(int));
            sellslist<<endl;
        }
    }
    cout<<"Do want to continue buy : 1(yes) ---  2(no)"<<endl;
    cin>>out;
    if (out == 1){Sell();}
    if (out == 2){menu();}

}
void SellBaseDate(void)
{
    int date1,date2;
    cout<<"-----------------------------------"<<endl<<endl;
    cout<<"Please enter first date '(YYYYMMDD)' :"<<endl;
    cin>>date1;
    cout<<"Please enter second date '(YYYYMMDD)' :"<<endl;
    cin>>date2;
    cout<<"Date------Name-----id-----Amount"<<endl<<endl;

    for (int i=0; i<indexsp ; i++)
    {
        if( date1 <= sp[i].date && sp[i].date <= date2)
        {
            cout<<sp[i].date<<"\t";
            cout<<sp[i].name<<"\t";
            cout<<sp[i].id<<"\t";
            cout<<sp[i].amount<<endl;
        }
    }




}


int main()
{

    //SetProduct();
    //SellBaseDate();
    menu();
    //cout<<indexsp<<endl;
    //int adad []={1,2,3,4,5,6};
    //cout<<p[0].name<<endl;
}
void menu(void)
{

    cout<<"-----------------------------------"<<endl;
    int num;
    cout<<"Please enter you number to continue :"<<endl;
    cout<<" 1)Sell\n 2)Inventory\n 3)Sells between two date\n 4)Exit"<<endl;
    cin>>num;
    switch(num)
    {
        case 1:

            ShowProduct();
            Sell();
            break;

        case 2:
            cout<<"Inventory :"<<endl;
            ShowProduct();
            menu();
            break;
        case 3:
            SellBaseDate();
            menu();
            break;
        case 4:
            update();
            break;

    }

}
