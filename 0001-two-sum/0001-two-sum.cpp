class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target);
};

vector<int> Solution::twoSum(vector<int>& nums, int target){
    int length = nums.size();
    vector<int> array;
    for(int i = 0; i < length; i++){
        for(int j = i; j < length; j++){
                if(i != j){
                    if((nums[i] + nums[j]) == target){
                        array.push_back(i);
                        array.push_back(j);
                        break;
                    }
                }
        }
    }
    return array;
};