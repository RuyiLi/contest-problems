import java.util.*;
import java.io.*;

public class Test {

	public static void main(String[] args) throws IOException {
		HashSet<String> set = new HashSet<String>();
		int N = readInt(), K = readInt(), W = readInt(); String arr[][] = new String[4][W]; int pts[] = new int[4];
		for(int i = 0; i<4; i++) for(int j = 0; j<W; j++) arr[i][j] = next(); 
		for(int j = 0; j<N*K; j++) {
//			System.out.println(j);
			String t = next();
			if(set.contains(t)) continue;
			set.add(t);
			for(int k = 0; k<4; k++) {
				for(int l = 0; l<W; l++) {
					if(arr[k][l].equals(t)) {pts[k]++; break;}
				}
			}
		}

		int max = Math.max(Math.max(pts[0], pts[1]), Math.max(pts[2], pts[3]));
		String name[] = {"Sayori", "Natsuki", "Yuri", "Monika"};
		for(int i = 0; i<4; i++) if(pts[i] == max) println(name[i]);
		exit();
	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static String next() throws IOException {
		while (st == null || !st.hasMoreTokens())
			st = new StringTokenizer(br.readLine().trim());
		return st.nextToken();
	}

	static long readLong() throws IOException {
		return Long.parseLong(next());
	}

	static float readFloat() throws IOException {
		return Float.parseFloat(next());
	}

	static boolean readBool() throws IOException {
		return Boolean.parseBoolean(next());
	}

	static short readShort() throws IOException {
		return Short.parseShort(next());
	}

	static byte readByte() throws IOException {
		return Byte.parseByte(next());
	}

	static int readInt() throws IOException {
		return Integer.parseInt(next());
	}

	static double readDouble() throws IOException {
		return Double.parseDouble(next());
	}

	static char readChar() throws IOException {
		return next().charAt(0);
	}

	static String readLine() throws IOException {
		return br.readLine().trim();
	}

	static PrintWriter pr = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

	static void print(Object o) {
		pr.print(o);
	}

	static void println(Object o) {
		pr.println(o);
	}

	static void flush() {
		pr.flush();
	}

	static void println() {
		pr.println();
	}

	static void exit() throws IOException {
		br.close();
		pr.close();
		System.exit(0);
	}
}
