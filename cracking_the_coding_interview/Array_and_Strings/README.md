### Hash Tables
- 해시테이블(Hash Table) : key와 value를 매핑하는 자료구조이다. (look up에 효율적)
- array of linked list와 a hash code function 사용
  1. key의 해시코드 계산 (int or long), 서로 다른 두 개의 key가 같은 hash code를 가질 수 있다. key 개수는 무한, 정수의 개수는 유한하기 때문에.
  2. 해시코드를 index에 매핑한다. ex) hash(key)%array_length, 서로 다른 두 개의 hash code가 같은 index를 가질 수 있다.
  3. index에는 key와 value의 링크드 리스트가 있다. index에 key와 value를 저장한다. (충돌 때문에 linked list를 사용해야한다. 같은 해시코드를 갖고 있는 two different keys가 있을 수 있다. or 서로 다른 해시코드를 갖고 있는 same index가 있을 수 있다.

- 충돌이 많다면, 최악의 runtime O(N) (N=키 개수)
- 하지만, 보통 충돌이 적을 것이라고  가정한다. lookup time = O(1)
- 이진 탐색 트리로 대체할 수 있다. 이때, lookup time = O(logN), 적은 공간 사용, 키값을 순서대로 반복할 수 있음


### ArrayList & Resizable Arrays
어떤 언어에서는 array는 automatically resizable하다.   
dynamically resizing할 때, ArrayList 사용한다.    
Array가 가득 찼을 때, array는 크기를 2배 늘린다. : O(n) time, amortized insertion time O(1)   
   
왜 amortized insertion runtime이 O(1)인가?   
array of size N 있다고 가정하자.   
N/2개 원소 복사, N/4개 원소 복사, N/8개 원소 복사.....1개 원소 복사   
N개의 원소를 넣기 위해 복사해야하는 횟수는 N/2+N/4+N/8+....+1로 N보다 작다.   
따라서, N개의 원소를 넣기 위해 걸리는 시간은 O(N)이다. 각 insertion에 걸리는 시간은 O(1)이다. (최악의 insertion time은 O(N)이다.)

### String Builder
문자열의 리스트를 이어 붙일 때, running time은 어떻게 될 것인가? 문자열들은 길이(x)가 똑같고, n개의 string이 있다.   
```
String joinWords(String[] words){
    String sentecne="";
    for (String w : words){
        sentence = sentece+w;
    }
  return sentence;
}
```
새로 연결할때마다, string의 새로운 복사본이 생긴다. First iteration x개의 캐릭터를 카피하고, Second iteration은 2x 개의 캐릭터를 카피한다.   
Total time : O(x+2x+3x+...+nx) = O(xn^2)
StringBuilder로 이 문제를 해결할 수 있다. StringBuilder는 resizable array를 생성하여, 필요한 경우에만 문자열을 복사해준다. 


