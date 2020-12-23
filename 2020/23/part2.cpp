#include <iostream>

#define CUPCOUNT 1000000
#define MOVES 10000000


using namespace std;


class Node {
    public:
        Node(int value): val(value), next(0), prev(0) {}
        int getVal() { return val; }
        Node* getNext() { return next; }
        void setNext(Node* n) { next = n; }
        Node* getPrev() { return prev; }
        void setPrev(Node* n) { prev = n; }
    private:
        int val;
        Node* next;
        Node* prev;
};


class NodeRing {
    public:
        NodeRing(): head(0) {}
        Node* getHead() { return head; }
        void append(int value) {
            Node* n = new Node(value);
            if (head == 0) {
                head = n;
                head->setNext(n);
                head->setPrev(n);
            } else {
                Node* tail = head->getPrev();
                n->setNext(head);
                n->setPrev(tail);
                tail->setNext(n);
                head->setPrev(n);
            }
        }
        void rotateLeft() {
            if (head) {
                head = head->getNext();
            }
        }
        void rotateRight() {
            if (head) {
                head = head->getPrev();
            }
        }
    private:
        Node* head;
};


class NodeCache {
    public:
        NodeCache() {
            nodes = new Node*[CUPCOUNT];
        }
        void put(int num, Node* node) {
            nodes[num-1] = node;
        }
        Node* get(int num) {
            return nodes[num-1];
        }
    private:
        Node** nodes;
};


void move(NodeRing* nr, NodeCache* nc) {
    Node* cur = nr->getHead();
    Node* p1 = cur->getNext();
    Node* p2 = p1->getNext();
    Node* p3 = p2->getNext();
    cur->setNext(p3->getNext());
    p3->getNext()->setPrev(cur);
    int dest = cur->getVal();
    while (1) {
        --dest;
        if (dest < 1) {
            dest = CUPCOUNT;
        }
        if (dest != p1->getVal() && dest != p2->getVal() && dest != p3->getVal()) {
            break;
        }
    }
    Node* ndest = nc->get(dest);
    ndest->getNext()->setPrev(p3);
    p3->setNext(ndest->getNext());
    ndest->setNext(p1);
    p1->setPrev(ndest);
    nr->rotateLeft();
}


int main(int argc, char** argv) {
    NodeRing* nr = new NodeRing();
    NodeCache* nc = new NodeCache();
    cout << "Please enter your input: ";
    uint64_t input;
    int inputLength = 0;
    cin >> input;
    while (input > 0) {
        nr->append(input % 10);
        nr->rotateRight();
        ++inputLength;
        input /= 10;
    }
    for (int i = inputLength + 1; i <= CUPCOUNT; ++i) {
        nr->append(i);
    }
    Node* n = nr->getHead();
    for (int i = 0; i < CUPCOUNT; ++i) {
        int num = n->getVal();
        nc->put(num, n);
        n = n->getNext();
    }
    for (int i = 1; i <= MOVES; ++i) {
        move(nr, nc);
    }
    n = nc->get(1);
    int v1 = n->getNext()->getVal();
    int v2 = n->getNext()->getNext()->getVal();
    cout << "result = " << v1 << " * " << v2 << " = " << ((int64_t) v1*v2) << endl;
}
