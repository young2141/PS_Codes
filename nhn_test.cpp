#include <iostream>
#include <vector>
#include <map>
using namespace std;

int obj_num, boat_size, driver_num, no_left_num, no_ride_num;
vector<string> obj,driver;
vector<vector<string>> no_left,no_ride;

void get_input(){
	cin >> boat_size;
	cin >> obj_num;
	obj.resize(obj_num);
	for (auto i = 0; i < obj_num; ++i) {
		cin >> obj[i];
	}
	cin >> driver_num;
	driver.resize(driver_num);
	for (auto i = 0; i < driver_num; ++i) {
		cin >> driver[i];
	}
	cin >> no_left_num;
	for (auto i = 0; i < no_left_num; ++i) {
		int n;
		cin >> n;
		vector<string> tmp(n);
		for (auto j = 0; j < n; ++j) {
			cin >> tmp[j];
		}
		no_left.push_back(tmp);
	}
	cin >> no_ride_num;	
	for (auto i = 0; i < no_ride_num; ++i) {
		int n;
		cin >> n;
		vector<string> tmp(n);
		for (auto j = 0; j < n; ++j) {
			cin >> tmp[j];
		}
		no_ride.push_back(tmp);
	}
}

int move(){
	
}

int main(int argc, char* argv[]) {

	get_input();
	

	return 0;
}