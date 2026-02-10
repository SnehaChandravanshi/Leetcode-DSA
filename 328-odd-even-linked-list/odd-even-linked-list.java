class Solution {
    public ListNode oddEvenList(ListNode head) {
         int n=1;
         if(head==null||head.next==null){
             return head;
         }
         ListNode curr=head.next.next;
         ListNode eve=head.next,odd=head,evenhead=eve;
         while(curr!=null){
             if(n%2==0){
                 eve.next=curr;
                 eve=eve.next;
             }
             else{
                 odd.next=curr;
                 odd=odd.next;
             }
             n++;
             curr=curr.next;
         }
            eve.next=null;
            odd.next=evenhead;
            return head;
    }
}