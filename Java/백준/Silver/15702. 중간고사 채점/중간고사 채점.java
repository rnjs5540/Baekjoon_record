import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int problemCount = Integer.parseInt(st.nextToken());
        int participantCount = Integer.parseInt(st.nextToken());

        int[] problemScores = new int[problemCount];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < problemCount; ++i) {
            problemScores[i] = Integer.parseInt(st.nextToken());
        }

        int[] participantIds =  new int[participantCount];
        int[] participantScores = new int[participantCount];
        for (int participantIndex = 0; participantIndex < participantCount; ++participantIndex) {
            st = new StringTokenizer(br.readLine());
            participantIds[participantIndex] = Integer.parseInt(st.nextToken());
            for (int problemIndex = 0; problemIndex < problemCount; ++problemIndex) {
                boolean isCorrect = st.nextToken().charAt(0) == 'O';
                if (isCorrect) {
                    participantScores[participantIndex] += problemScores[problemIndex];
                }
            }
        }

        int maxScore = -1;
        int maxScoreParticipantId = -1;
        for (int participantIndex = 0; participantIndex < participantCount; ++participantIndex) {
            if (maxScore == participantScores[participantIndex]) {
                maxScoreParticipantId = Math.min(maxScoreParticipantId, participantIds[participantIndex]);
            }
            else if (maxScore < participantScores[participantIndex]) {
                maxScoreParticipantId = participantIds[participantIndex];
                maxScore = participantScores[participantIndex];
            }
        }

        System.out.println(maxScoreParticipantId + " " + maxScore);
    }
}
