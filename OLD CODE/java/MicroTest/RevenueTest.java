// package MicroTest;

// import static org.junit.jupiter.api.Assertions.*;

// import org.junit.jupiter.api.BeforeEach;
// import org.junit.jupiter.api.Test;

// import Micro.*;

// public class RevenueTest {
//     Revenue rev = new Revenue();

//     @BeforeEach
//     public void setup() {
//         rev.clear();
//     }

//     @Test
//     public void testChanges() {
//         assertEquals(0, rev.getPrice());
//         assertEquals(0, rev.getQuantity());
//         assertEquals(0, rev.getRevenue());
        
//         rev.changePrice(2);
//         assertEquals(2, rev.getPrice());
//         assertEquals(0, rev.getQuantity());
//         assertEquals(0, rev.getRevenue());
        
//         rev.changeQuantity(5);
//         assertEquals(2, rev.getPrice());
//         assertEquals(5, rev.getQuantity());
//         assertEquals(10, rev.getRevenue());
//     }

//     @Test
//     public void testEq() {
//         assertEquals("\'Revenue\' = \'price\' x \'quantity\'", rev.getEquation());
//         assertEquals("0.0 = 0.0 x 0.0", rev.filledEq());
//     }
// }
